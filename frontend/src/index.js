import React from 'react';
import ReactDOM from 'react-dom';
import {
    BrowserRouter as Router,
    Switch,
    Route,

} from "react-router-dom";

import history from './history';

// import All from "./pages/Page";
import New from "./pages/Page";
import Rank from "./pages/Page";
import Starred from "./pages/Page";
import Page from "./pages/Page";
import Container from "./components/Container";
import getPageNumber from "./util/pageNumber";

function NotFound() {
    return (
        <div>
            <h1>That page was not found</h1>
        </div>
    );
}

function All(props) {
    const { match } = props;

    return (
        <Container type={`all/${match.params.slug}/`} page={getPageNumber(match.params.page)} />
    );
}


ReactDOM.render(
  <React.StrictMode>
    <Router>
        <Switch>
            {/*<Route*/}
            {/*    path="/:slug/new/:page(\d+)?"*/}
            {/*    component={New}*/}
            {/*/>*/}
            <Route
                path="/:slug/all/:page(\d+)?"
                component={All}
            />
            {/*<Route*/}
            {/*    path="/:slug/rank/:page(\d+)?"*/}
            {/*    component={Rank}*/}
            {/*/>*/}
            {/*<Route*/}
            {/*    path="/:slug/starred/:page(\d+)?"*/}
            {/*    component={Starred}*/}
            {/*/>*/}
            {/*<Route*/}
            {/*    path="/:slug/:page(\d+)?"*/}
            {/*    component={Page}*/}
            {/*/>*/}
            <Route path="" component={NotFound} />
        </Switch>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);