// @flow
"use strict";
import React from "react";
import Spinner from "react-spinkit";

class Loader extends React.PureComponent {
  render() {
    return (
      <Spinner style={{"visibility": this.props.visibility}} name="cube-grid"/>
    );
  }
}

export default Loader;
