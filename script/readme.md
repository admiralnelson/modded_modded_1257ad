functions and procedures
========================
Script body goes to these sub directory, in each directory there are files that represent an object. \n
for example, party_calculate_faggotry_level that takes in: party_no, and returns a certain value ranging [0,100]. \n
because that script returns a value and it "resembles" an method object of party, it should reside on /functions/party.py \n
```
  ...
  ablablablabalbalblaa
  
  # script_party_calculate_faggotry_level 
  # calculates party faggotry level so it can be used for meme purpose
  # INPUT: arg1 = party_no
  # OUTPUT: reg0 = faggotry level [0,100]
  party_calculate_faggotry_level = (
    "party_calculate_faggotry_level"
    [
      (store_script_param, ":party_id", 1),
      ....
    ])
```


function : a script that returns values \n
conditional_function : a cf script that doesn't return values, it is used as conditional checks (can fail) \n
procedure: a script that returns no values \n
 
NOTE: there are cf scripts in function, because they do return value, but also act as conditional function
