import * as React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import SideMenu from "./molecules/sidemenu"
import FilterHelpView from "./organisms/filter_help_view"
import ImageRepository from '../model/image_repository';




export default function Header() {
    const [open, setOpen] = React.useState(false)
    const [filterHelpList, setFilterHelpList] = React.useState([])

    React.useEffect(() => {
        let cleanedUp = false;

        new ImageRepository().getFilterHelpList().then((response) => {
            if (cleanedUp) {
                return;
            }
            setFilterHelpList(response.data.filter_help_list)
        }).catch((error) => {
            if (cleanedUp) {
                return;
            }
            console.log(error.response)
            setFilterHelpList([])
        });
        const cleanUp = () => {
            cleanedUp = true
        }
        return cleanUp
    }, [])

    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" style={{ width: "100%" }}>
                    画像処理ツール
                </Typography>
                <IconButton
                    color="inherit"
                    aria-label="open drawer"
                    edge="end"
                    onClick={() => setOpen(!open)}>
                    <MenuIcon />
                </IconButton>
            </Toolbar>
            <SideMenu open={open} onClose={() => setOpen(false)} width={"50vw"}>
                <FilterHelpView filterHelpList={filterHelpList} />
            </SideMenu>
        </AppBar>
    );
}