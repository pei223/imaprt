# Create your views here.
from typing import List, Dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
import traceback

from .models import *
from . import media_manager
from .models.filtering.help import filter_help_service

KEY_FILTER_PARAMS = "filter_params"


@api_view(['POST'])
def filter_chain(request):
    # NOTE QueryDictだとリスト中身の辞書がなぜかうまく動かない
    filter_params = dict(request.POST).get(KEY_FILTER_PARAMS)
    if filter_params is None:
        raise ParseError('Require filter_params.')

    # ファイル周り
    file = request.FILES.get('file')
    if file is None:
        raise ParseError('Require file.')
    origin_file_name = file.name
    origin_image = media_manager.uploaded_file_to_cvimage(file)

    # フィルタ手法の決定, パラメータが間違っているならエラーメッセージ
    error_messages = []
    filtering_ls = [Origin(), ]
    for i, filter_param in enumerate(filter_params):
        try:
            filtering = filtering_factory.create(filter_param)
            filtering_ls.append(filtering)
        except Exception as error:
            print(filter_param)
            traceback.print_exc()
            error_message = f"[{i + 1}]: {error}"
            error_messages.append(error_message)
    if len(error_messages) > 0:
        return Response(error_messages, status.HTTP_400_BAD_REQUEST)

    # フィルタリング適用
    media_manager.clear_images_regularly()
    image_info_ls, code_generator = filtering_service.apply_chain_filtering(origin_image, origin_file_name,
                                                                            filtering_ls)
    return Response(arrange_response(image_info_ls, code_generator), status=status.HTTP_200_OK)


@api_view(['POST'])
def filter_batch(request):
    # NOTE QueryDictだとリスト中身の辞書がなぜかうまく動かない
    filter_params = dict(request.POST).get(KEY_FILTER_PARAMS)
    if filter_params is None:
        raise ParseError('Require filter_params.')

    # ファイル周り
    file = request.FILES.get('file')
    if file is None:
        raise ParseError('Require file.')
    origin_file_name = file.name
    origin_image = media_manager.uploaded_file_to_cvimage(file)

    # フィルタ手法の決定, パラメータが間違っているならエラーメッセージ
    error_messages = []
    filtering_ls = [Origin(), ]
    for i, filter_param in enumerate(filter_params):
        try:
            filtering = filtering_factory.create(filter_param)
            filtering_ls.append(filtering)
        except Exception as error:
            error_message = f"[{i + 1}]: {error}"
            error_messages.append(error_message)
    if len(error_messages) > 0:
        return Response({"errors": error_messages}, status.HTTP_400_BAD_REQUEST)

    # フィルタリング適用
    media_manager.clear_images_regularly()
    image_info_ls, code_generator = filtering_service.apply_batch_filtering(origin_image, origin_file_name,
                                                                            filtering_ls)
    return Response(arrange_response(image_info_ls, code_generator), status=status.HTTP_200_OK)


@api_view(['GET'])
def help_list(request):
    return Response({"filter_help_list": filter_help_service.generate_help_json()})


def arrange_response(filter_image_info_ls: List[FilterImageInfo], code_generator: CodeGenerator) -> Dict:
    result = list(map(lambda image_info: image_info.to_dict(), filter_image_info_ls))
    return {"result": result, "code": code_generator.generate()}
