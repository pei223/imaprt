import { makeStyles } from '@material-ui/styles';


export const commonStyles = makeStyles((theme) => ({
    contentsContainer: {
        backgroundColor: "#eeeeee",
        overflowY: "scroll",
    },
    contentBlock: {
        marginBottom: "10px",
        backgroundColor: "white"
    }
}));