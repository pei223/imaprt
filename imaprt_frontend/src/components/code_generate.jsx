import * as React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import IconButton from '@material-ui/core/IconButton';
import VisibilityIcon from '@material-ui/icons/Visibility';
import Modal from '@material-ui/core/Modal'
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/styles';
import TextField from '@material-ui/core/TextField';
import { commonStyles } from './common_styles';


const useStyles = makeStyles((theme) => ({
    modalWindow: {
        position: 'absolute',
        left: "10%",
        top: "10%",
        height: "80%",
        width: "80%",
        backgroundColor: "white",
        border: "none",
        padding: "20px",
    },
    codeArea: {
        width: "100%"
    }
}));

export default function CodeGenerate(props) {
    const classes = useStyles();
    const commonClasses = commonStyles();

    const [open, setOpen] = React.useState(false);

    return (
        <div>
            <Card className={commonClasses.contentBlock}>
                <CardContent>
                    <Grid container>
                        <Grid item xs={10}>
                            <p>自動生成コード</p>
                        </Grid>
                        <Grid item xs={2}>
                            <IconButton aria-label="delete" edge="end" onClick={() => setOpen(true)}>
                                <VisibilityIcon fontSize="large" />
                            </IconButton>
                        </Grid>
                    </Grid>
                </CardContent>
            </Card>
            <Modal
                open={open}
                onClose={() => setOpen(false)}
                aria-labelledby="simple-modal-title">
                <div className={classes.modalWindow}>
                    <h2 id="simple-modal-title">自動生成コード</h2>
                    <TextField
                        className={classes.codeArea}
                        value={props.code}
                        placeholder="params"
                        multiline
                        variant="outlined"
                        rows={30}
                        rowsMax={30} />
                </div>
            </Modal>
        </div>
    )
}