import React from 'react';
import { RouteComponentProps } from 'react-router';

import Container from '../components/Container';

import getPageNumber from '../util/pageNumber';

function New(props) {
    const { match } = props;

    return (
        <Container type={`/new/${match.params.slug}/`} page={getPageNumber(match.params.page)} />
    );
}

export default New;