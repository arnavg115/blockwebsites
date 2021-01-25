# blockwebsites
A tool that helps to block websites
## how to
Clone the repo
```
$ git clone https://github.com/arnavg115/blockwebsites.git
```
In the terminal change your directory to the new repo folder
```
$ cd blockwebsites
```
Change the permisions on the file
```
chmod +x blockwebsites
```
Then you can
```
$ ./blockwebsites <website>
```
enter the website you would like to block. For example, google.com.
```
$ ./blockwebsites google.com
```
This may take a few minutes to actually implement.
## To unblock websites
First give the scripts the permision
```
$ chmod +x unblockwebsites
```
then in the terminal type
```
$ ./unblockwebsites <website>
```
## How does it work?
This script modifies a document found in unix and linux systems at /etc/hosts. It adds websites to this document then it flushes your dns cache. To unblock it just removes the entries that it gave. If somehow your /etc/hosts gets messed up I reccomend doing something like
```
sudo nano /etc/hosts
```
then using <a href = "https://gist.github.com/ghoneycutt/e531984406b4b86ace687ea8958a6dc3"> this list</a> copy paste your defaults. Then do ctrl-o and then enter to save and ctrl-x to exit.Then type 
```
sudo dscacheutil -flushcache
``` 
to flush your DNS cache once more and it shoud be reset.
## Eligibility
<strong>Works only on  linux and unix(MacOs) systems.</strong>
