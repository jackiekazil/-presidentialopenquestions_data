# Data in this folder

**Files with 'data_$date_$time.json'** - These files are data pulls from
presidential debate questions.

**state_abbr_color.json** - This is a hand made list of full name, state abbr,
and party standing.

**state_pop.csv** - This is a [population estimate file](https://www.census.gov/popest/data/state/asrh/2015/files/SCPRC-EST2015-18+POP-RES.csv) from Census for the 2015 population.

**state_combined_list.json** - This file is created by create_state_pop_dataset.py
file one folder up. It combines state_abbr_color.json and state_pop.csv. This
file uses the over 18 population to insure that children unable to vote are not
counted.
