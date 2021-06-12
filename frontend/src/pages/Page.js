import React from 'react';
import { RouteComponentProps } from 'react-router';

import Container from '../components/Container';

import getPageNumber from '../util/pageNumber';

function Page(props) {
    const { match } = props;

    return (
        <Container type={`/${match.params.slug}/`} page={getPageNumber(match.params.page)} />
    );
}

export default Page;