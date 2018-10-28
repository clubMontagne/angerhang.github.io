# Prerequisites (for mac)

* Python 3.7.0
* pip
* brew

# Installation

1. Create directory `mkdir -p ~/workspace/`
1. Clone this repo `git@github.com:clubMontagne/clubMontagne.github.io.git ~/workspace/clubMontagne.github.io`
1. Create virtual environment `virtualenv ~/workspace/env.clubMontagne.Monbers`
1. Activete it `source ~/workspace/env.clubMontagne.Monbers/bin/activate`
1. Install required packages `pip install -r ~/workspace/clubMontagne.github.io/monbers/requirements.txt`
1. Install geckodriver `brew install geckodriver` (used for status verification)

# Running the script

1. Go to https://docs.google.com/spreadsheets/d/1mkcOwDxQwSUXWN5w6_dy_oAxpYAxe4OIuKcKPbplLxk/edit?usp=sharing and File -> Download as -> Comma-separated values. Name file "new.csv".
1. `cd ~/workspace/clubMontagne.github.io/monbers/code`
1. Clean files from the previous run `git clean -Xf`
1. Activete virtual environment `source ~/workspace/env.clubMontagne.Monbers/bin/activate`
1. Run script `python verifyStatus.py ~/Downloads/new.csv ~/workspace/clubMontagne.github.io/members/img/`
1. Commit status changes and push to the repo `git add ../../members/`, `git commit`, `git push`

Send emails

1. Open new.csv and remove lines where Email_sent is "TRUE"
1. Open verifyStatus.py and uncomment section "5. send QR code to the email" and a line below it.
1. Run script `python verifyStatus.py ~/Downloads/new.csv ~/workspace/clubMontagne.github.io/members/img/`
1. Open final.csv and copy value from 3 last columns (Payment, Email_sent and If_complete) to https://docs.google.com/spreadsheets/d/1mkcOwDxQwSUXWN5w6_dy_oAxpYAxe4OIuKcKPbplLxk/edit?usp=sharing