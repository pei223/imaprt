import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/styles';
import FolderOpenIcon from '@material-ui/icons/FolderOpen';
import CachedIcon from '@material-ui/icons/Cached';
import SendIcon from '@material-ui/icons/Send';
import { commonStyles } from './common_styles';


const useStyles = makeStyles({
    paramsArea: {
        width: "100%",
        height: "70%",
    },
    formBlock: {
        paddingTop: "10px",
        paddingBottom: "10px",
        borderBottom: "1px solid #aaaaaa"
    },
    filePicker: {
        opacity: "0",
        appearance: "none",
        position: "absolute",
    },
    errorText: {
        color: "red",
        fontSize: "0.75rem"
    }
});

export default function Form(props) {
    const classes = useStyles();
    const commonClasses = commonStyles();

    return (
        <Card className={commonClasses.contentBlock}>
            <CardContent>
                <Typography color="textSecondary" gutterBottom>
                    Params
                </Typography>
                <TextField
                    value={props.params}
                    onChange={(e) => props.onParamsChanged(e.target.value)}
                    className={classes.paramsArea}
                    placeholder="params"
                    multiline
                    helperText={props.paramsError}
                    error={props.paramsError !== ""}
                    rows={25}
                    rowsMax={25} />

                <div className={classes.formBlock}>
                    <div>
                        <Button variant="contained" color="primary">
                            <FolderOpenIcon />&nbsp;&nbsp;&nbsp;Pick file
                        <input type="file" className={classes.filePicker} name="file" accept=".jpg,.jpeg,.JPG,.png"
                                onChange={(e) => props.onFileChanged(e.target.value)} />
                        </Button>
                        {props.selectedFile}
                        <p className={classes.errorText}>
                            {props.fileError}
                        </p>
                    </div>
                    <Button variant="contained" color="primary" onClick={() => props.onProcessTypeChanged((props.processType + 1) % 2)}>
                        <CachedIcon />&nbsp;&nbsp;&nbsp; {props.processType === 1 ? "フィルタ重ね" : "一括処理"}
                    </Button>
                </div>

                <div style={{ marginTop: "20px", width: "100%", textAlign: "center" }}>
                    <Button variant="contained" color="primary" style={{ width: "100%" }} onClick={() => props.submit()}>
                        <SendIcon />&nbsp;&nbsp;&nbsp; 実行
                    </Button>
                </div>
            </CardContent>
        </Card>
    )
}