import { Route, BrowserRouter as Router } from 'react-router-dom';

import Homepage from './pages/Homepage';
import React from 'react';
import { Switch } from 'react-router-dom';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Homepage} />
      </Switch>
    </Router>
  );
};

export default App;
