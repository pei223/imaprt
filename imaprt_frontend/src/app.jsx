import * as React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/styles';

import Header from './components/header'
import Form from './components/form'
import ResultImages from './components/result_images'
import CodeGenerate from './components/code_generate'
import { commonStyles } from './components/common_styles';
import ImageRepository from './model/image_repository';
import {DEFAULT_PARAMS_JSON} from './model/filtering_rule'


const useStyles = makeStyles({
    container: {
        marginTop: "5px"
    }
  });
export default function App() {
    const [selectedFile, setFile] = React.useState();
    const [fileError, setFileError] = React.useState("");

    const [params, setParams] = React.useState(JSON.stringify(DEFAULT_PARAMS_JSON, null, ' '));
    const [paramsError, setParamsError] = React.useState("");

    const [processType, setProcessType] = React.useState(1);
    const [code, setCode] = React.useState("");

    const [resultImages, setResultImages] = React.useState([]);

    const classes = useStyles();
    const commonClasses = commonStyles();

    const validateParams = () => {
        let paramsErrorMessage = ""
        try {
            let paramsJson = JSON.parse(params)
            if (!Array.isArray(paramsJson)) {
                throw "Error"
            }
        } catch {
            paramsErrorMessage = "JSON形式が正しくありません。JSON配列にしてください。"
        }
        return paramsErrorMessage
    }

    const submit = () => {
        let fileSelectDom = document.getElementsByName("file")[0].files[0];
        let fileErrorMessage = fileSelectDom === undefined ? "ファイルを選択してください。" : ""
        setFileError(fileErrorMessage)

        let paramsErrorMessage = validateParams()
        setParamsError(paramsErrorMessage)
        
        if (paramsErrorMessage !== "" || fileErrorMessage !== "") {
            return
        }

        let onSucceed = (response) => {
            setCode(response.data.code)
            setResultImages(response.data.result)
        }
        let onError = (error) => {
            if (error.response.status === 400) {
                setParamsError(error.response.data.join("\n"))
                return
            }
            window.alert(error.response.data)
        }
        if (processType === 1) {
            new ImageRepository().calcChainFiltering(params, fileSelectDom).then(onSucceed).catch(onError);
        } else {
            new ImageRepository().calcBatchFiltering(params, fileSelectDom).then(onSucceed).catch(onError);
        }
    }

    return (
        <div className={commonClasses.contentsContainer}>
            <Header />
            <Grid container spacing={3} className={classes.container}>
                <Grid item xs={4}>
                    <Form 
                        params={params}
                        onParamsChanged={(value) => {setParams(value);setParamsError("");}}
                        paramsError={paramsError}
                        processType={processType}
                        onProcessTypeChanged={(value) => setProcessType(value)}
                        selectedFile={selectedFile}
                        onFileChanged={(value) => {
                            // キャンセルを考慮
                            if (value === null || value === "" || value === undefined)
                                return;
                            setFile(value)
                            setFileError("")
                        }}
                        fileError={fileError}
                        submit={() => submit()} />
                    <p style={{marginBottom: "5px"}}></p>
                    <CodeGenerate code={code} />
                </Grid>
                <Grid item xs={8}>
                    <ResultImages data={resultImages} />
                </Grid>
            </Grid>
        </div>
    );
  }