### 1.6.0 (February 4, 2017)
* Changed timing on the delayed popup to 11s.
* Added a parent function to the delayed popup and added the timing there; this avoids storing the popup_show local storage flag without actually firing the script; if the visitor does not see the popup, on the first page he/she visits, they still have the chance of seeing the popup in a different page.
* Delayed popup now also checks for exitintent_show flag in local storage to avoid overriding conflict for the visitor.

### 1.5.0 (February 5, 2016)

* Replaced hubspot-templates with local-hubl-server. We are depcrating the COS Uploader tool in place for the COS FTP.


### 1.0.0 (April 4, 2015)

* Updated the .gitignore file; node_modules will not be tracked anymore. 
  When cloning the framework, you will need to run npm install command to 
  add any node module dependencies; this lowers the file size of the framework 
  and will help avoid any cross platform errors. 
* Moved all grid related code from patterns.scss to grid-settings.scss.
* Initiated a README.md file.