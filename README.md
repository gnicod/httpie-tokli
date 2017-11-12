# httpie-tokli
oaut2 plugin for httpie using tokli

## Usage
Already have an entry for test_dev in your ~/.config/tokli/apis.yaml ?
```
http -v --auth-type=tokli -a test_dev: get "http://localhost/api"
```
Wanna force the creation and use of a new token ?
```
http -v --auth-type=tokli -a test_dev:refresh get "http://localhost/api"
```
