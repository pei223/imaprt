const axios = require('axios')
import {API_URL} from '../consts/server';
axios.defaults.baseURL = API_URL


const config = {
    headers: {
        'content-type': 'multipart/form-data'
    }
}

export default class ImageRepository {
    async calcChainFiltering(params: string, imageFile: any) {
        return await this.postFiltering(params, imageFile, "/imaprt_api/filter_chain")
    }

    async calcBatchFiltering(params: string, imageFile: any) {
        return await this.postFiltering(params, imageFile, "/imaprt_api/filter_batch")
    }

    async postFiltering(params: string, imageFile: any, url: string) {
        let formData = new FormData()
        let paramsJson = JSON.parse(params)
        paramsJson.forEach(element => {
            formData.append("filter_params", JSON.stringify(element))
        });

        // formData.append("filter_params", JSON.stringify(paramsJson))
        formData.append("file", imageFile)
        let result = await axios.post(url, formData, config)
        return result
    }
}