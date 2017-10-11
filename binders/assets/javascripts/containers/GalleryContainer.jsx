// @flow
"use strict";

import React from "react";
import {Grid} from "react-bootstrap";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import {cyan500} from "material-ui/styles/colors";
import getMuiTheme from "material-ui/styles/getMuiTheme";
import BinderGallery from "../components/BinderGallery"
// import appSetup from "../commons"


const muiTheme = getMuiTheme({
  palette: {
    canvasColor: cyan500,
  },
});


class GalleryContainer extends React.PureComponent {
  constructor(props) {
    super(props);
    // this.onChange = this.onChange.bind(this);
    this.state = {
      binderCards: testBinderData,
      loader_visibility: "visible"
    }
  }

  render() {
    return (
      <MuiThemeProvider muiTheme={muiTheme}>
        <Grid>
          <div style={{"marginTop": "75px"}}>
            <BinderGallery binderCards={this.state.binderCards}/>
          </div>
        </Grid>
      </MuiThemeProvider>
    )
  }
}

export default GalleryContainer;
