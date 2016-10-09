import csv
import json

with open('data/state_abbr_color.json') as data_file:
    state_abbr_color = json.load(data_file)

state_pop = []
with open('data/state_pop.csv') as data_file:
    reader = csv.DictReader(data_file)
    for r in reader:
        state_pop.append([r['NAME'], r['POPEST18PLUS2015']])


# this is horrible, but this is about getting it done not
# optimizing, because the data is so small
new_records = []
for sp in state_pop:
    sp_state, sp_pop = sp
    sp_state = sp_state.strip('.').lower()
    for sac in state_abbr_color:
        sac_state, abbr, side = sac

        if sac_state.lower() == sp_state:
            new_records.append([abbr, sp_pop, side])

with open('data/state_combined_list.json', 'w') as outfile:
    json.dump(new_records, outfile)
