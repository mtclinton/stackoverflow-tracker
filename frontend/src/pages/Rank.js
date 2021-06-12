import React from 'react';
import { RouteComponentProps } from 'react-router';

import Container from '../components/Container';

import getPageNumber from '../util/pageNumber';

function Rank(props) {
    const { match } = props;

    return (
        <Container type={`/rank/${match.params.slug}/`} page={getPageNumber(match.params.page)} />
    );
}

export default Rank;