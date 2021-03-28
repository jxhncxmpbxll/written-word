import React, { Component } from 'react';
import Logo from './logo';
import InputURL from './inputURL';
import ProgressBar from './progressBar';
import DownloadTextButton from './downloadButton';

import axios from 'axios';

import styles from './styles/app.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showProgress: false,
      showDownload: false,
      inputURL: '',
    }
    this.handleURLInput = this.handleURLInput.bind(this);
    this.handleShowProgress = this.handleShowProgress.bind(this);
  }

  handleURLInput(text) {
    this.setState({inputURL: text});
  }

  handleShowProgress() {
    this.setState({showProgress: true});
  }

  render() {
    return (
      <div className={styles.mainContainer}>
        <div className={styles.appContainer}>
        <Logo/>
        <InputURL
          handleInput={this.handleURLInput}
          handleShowProgress={this.handleShowProgress}/>
          {this.state.showProgress ? <ProgressBar/> : <div style={{height: '25px'}}/>}
          {this.state.showDownload ? <DownloadTextButton/> : null}
        </div>
      </div>
    )
  }
}

export default App;
