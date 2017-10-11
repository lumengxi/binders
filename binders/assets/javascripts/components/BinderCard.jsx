// @flow
"use strict";
import React from "react";
import {Card, CardText, CardTitle} from 'material-ui/Card';
import randomColor from 'randomcolor';

class BinderCard extends React.PureComponent {

  constructor(props) {
    super(props);
  }

  render() {
    let binderCard = this.props.binderCard;
    return(
      <Card
        style={{backgroundColor: randomColor({luminosity: 'light', alpha: 0.1})}}
        expandable={true}
        expanded={false}
      >
        <CardTitle
          title={binderCard.name}
          subtitle={binderCard.document_type}
          actAsExpander={true}
        />
        <CardText style={{fontSize: '15px'}}>
          <b>Owner: </b>{binderCard.owner}
          <br />
          <b>Description: </b>{binderCard.description}
          <br />
          <b>Language: </b>{binderCard.lang}
          <br />
          <b>Repository: </b><a href={binderCard.url}>{binderCard.url}</a>
          <br />
          <b>Documentation: </b><a href={binderCard.doc_link}>{binderCard.doc_link}</a>

        </CardText>
      </Card>
    )
  }
}

export default BinderCard;
