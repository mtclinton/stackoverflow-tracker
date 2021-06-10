import React from 'react';
import { RouteComponentProps } from 'react-router';

import Container from '../components/Container';

import getPageNumber from '../util/pageNumber';

function All(props) {
    const { match } = props;

    return (
        <Container type={`/all/${match.params.slug}/`} page={getPageNumber(match.params.page)} />
    );
}

export default All;