// @flow
"use strict";

import React from "react";
import StackGrid, {transitions} from "react-stack-grid";
import BinderCard from "./BinderCard";

const {scaleDown} = transitions;

class BinderGallery extends React.PureComponent {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <StackGrid
        appear={scaleDown.appear}
        appeared={scaleDown.appeared}
        enter={scaleDown.enter}
        entered={scaleDown.entered}
        leaved={scaleDown.leaved}
        monitorImagesLoaded={true}
        columnWidth={300}
        gutterWidth={20}
      >
        {this.props.binderCards.map((binderCard, i) => {
          return (
            <div id={i} style={{"marginTop": "10px", "marginBottom": "10px"}}>
              <BinderCard binderCard={binderCard}/>
            </div>
          )
        })}
      </StackGrid>
    );
  }
}

export default BinderGallery;
