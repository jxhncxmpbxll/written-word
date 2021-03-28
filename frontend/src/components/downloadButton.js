import React from 'react';

import { download } from '../icons/icons';
import styles from './styles/downloadButton.css';

const DownloadTextButton = (props) => {

  return (
    <div className={styles.downloadContainer}>
      <button
        className={styles.downloadButton}
        >DOWNLOAD</button>
      <div className={styles.downloadIconContainer}>{download}</div>
    </div>
  )
}

export default DownloadTextButton;