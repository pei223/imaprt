import * as React from 'react';
import Card from '@material-ui/core/Card';
import Typography from '@material-ui/core/Typography';
import CardContent from '@material-ui/core/CardContent';
import { makeStyles } from '@material-ui/styles';
import Grid from '@material-ui/core/Grid';
import { API_URL } from '../consts/server';
import AddIcon from '@material-ui/icons/AddCircle';
import MinusIcon from '@material-ui/icons/RemoveCircle';
import IconButton from '@material-ui/core/IconButton';
import { commonStyles } from './common_styles';


const useStyles = makeStyles({
    description: {
        textAlign: "center"
    },
    image: {
        width: "100%"
    },
    imagesArea: {
        height: "80vh",
        overflowY: "scroll"
    }
});

export default function ResultImages(props) {
    const [zoomLevel, setZoomLevel] = React.useState(4)

    const incrementZoomLevel = () => {
        if (zoomLevel === 12) {
            return
        }
        setZoomLevel(zoomLevel + 1)
    }
    const decrimentZoomLevel = () => {
        if (zoomLevel === 1) {
            return
        }
        setZoomLevel(zoomLevel - 1)
    }

    const classes = useStyles();
    const commonClasses = commonStyles();

    let imageNodes = ""
    if (props.data.length === 0) {
        imageNodes = "画像とParamsを設定して実行ボタンを押してください"
    } else {
        imageNodes = props.data.map((data) => {
            return (
                <Grid item xs={zoomLevel} key={data.url}>
                    <img src={API_URL + data.url} className={classes.image} />
                    <p className={classes.description}>{data.title}<br/>{data.description}</p>
                </Grid>
            )
        })
        imageNodes = (
            <Grid container spacing={3}>
                {imageNodes}
            </Grid>
        )
    }

    return (
        <Card className={commonClasses.contentBlock}>
            <CardContent className={classes.imagesArea}>
                <div>
                    <Grid container>
                        <Grid item xs={10}>
                            <Typography color="textSecondary" gutterBottom>
                                Results
                            </Typography>
                        </Grid>
                        <Grid item xs={2}>
                            <IconButton onClick={incrementZoomLevel}>
                                <AddIcon />
                            </IconButton>
                            {zoomLevel}
                            <IconButton onClick={decrimentZoomLevel}>
                                <MinusIcon />
                            </IconButton>
                        </Grid>
                    </Grid>
                </div>
                {imageNodes}
            </CardContent>
        </Card>
    )
}