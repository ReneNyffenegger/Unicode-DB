#!/usr/bin/python3
# vi: foldmethod=marker foldmarker={{{,}}}

import os
import sqlite3

db_name = 'unicode.db'
if os.path.isfile(db_name):
   os.remove(db_name)

db  = sqlite3.connect(db_name)
cur = db.cursor()

cur.execute("""
create table normative_category (
  abbreviation primary key,
  description,
  normative_informative
) """)

cur.executemany('insert into normative_category values (?, ?, ?)', [ # {{{
  ('Lu', 'Letter, Uppercase'                                                       , 'norm'),
  ('Ll', 'Letter, Lowercase'                                                       , 'norm'),
  ('Lt', 'Letter, Titlecase'                                                       , 'norm'),
  ('Mn', 'Mark, Non-Spacing'                                                       , 'norm'),
  ('Mc', 'Mark, Spacing Combining'                                                 , 'norm'),
  ('Me', 'Mark, Enclosing'                                                         , 'norm'),
  ('Nd', 'Number, Decimal Digit'                                                   , 'norm'),
  ('Nl', 'Number, Letter'                                                          , 'norm'),
  ('No', 'Number, Other'                                                           , 'norm'),
  ('Zs', 'Separator, Space'                                                        , 'norm'),
  ('Zl', 'Separator, Line'                                                         , 'norm'),
  ('Zp', 'Separator, Paragraph'                                                    , 'norm'),
  ('Cc', 'Other, Control'                                                          , 'norm'),
  ('Cf', 'Other, Format'                                                           , 'norm'),
  ('Cs', 'Other, Surrogate'                                                        , 'norm'),
  ('Co', 'Other, Private Use'                                                      , 'norm'),
  ('Cn', 'Other, Not Assigned (no characters in the file have this property'       , 'norm'),

  ('Lm', 'Letter, Modifier'                                                        , 'info'),
  ('Lo', 'Letter, Other'                                                           , 'info'),
  ('Pc', 'Punctuation, Connector'                                                  , 'info'),
  ('Pd', 'Punctuation, Dash'                                                       , 'info'),
  ('Ps', 'Punctuation, Open'                                                       , 'info'),
  ('Pe', 'Punctuation, Close'                                                      , 'info'),
  ('Pi', 'Punctuation, Initial quote (may behave like Ps or Pe depending on usage)', 'info'),
  ('Pf', 'Punctuation, Final quote (may behave like Ps or Pe depending on usage)'  , 'info'),
  ('Po', 'Punctuation, Other'                                                      , 'info'),
  ('Sm', 'Symbol, Math'                                                            , 'info'),
  ('Sc', 'Symbol, Currency'                                                        , 'info'),
  ('Sk', 'Symbol, Modifier'                                                        , 'info'),
  ('So', 'Symbol, Other'                                                           , 'info')

]) # }}}

db.commit()

# jcur.execute("""
# jcreate table normative_category (
# j  abbreviation,
# j  description ,
# j  primary key abbreviation
# j) """)

with open('UnicodeData.txt') as ucdat_file: # {{{
     for ucdat_line in ucdat_file:

         ucdat_line = ucdat_line.rstrip('\n\r')
         ucdat_elem = ucdat_line.split(';') # {{{

         code_value                    = ucdat_elem[ 0]
         character_name                = ucdat_elem[ 1]
         general_category              = ucdat_elem[ 2]
         canonical_combining_classes   = ucdat_elem[ 3]
         bidirectional_category        = ucdat_elem[ 4]
         character_decomposing_mapping = ucdat_elem[ 5]
         decimal_digit_value           = ucdat_elem[ 6]
         digit_value                   = ucdat_elem[ 7]
         numeric_value                 = ucdat_elem[ 8]
         mirrored                      = ucdat_elem[ 9]
         unicode_1_value               = ucdat_elem[10] # Old name for character as published in Unicode 1.0 -  only provided if significantly different from the Unicode 3.0 name 
         comment_10646                 = ucdat_elem[11]
         uppercase_mapping             = ucdat_elem[12]
         lowercase_mapping             = ucdat_elem[13]
         titlecase_mapping             = ucdat_elem[14]

         code_value_int                = int(code_value, 16)

         # }}}

    #    if character_name[0] == '<':
    #       print(str(code_value_int) + ': ' + character_name + ' - ' + unicode_1_value)

    #    if numeric_value != '':
    #       print(character_name, numeric_value)

    #    if character_name == 'VULGAR FRACTION ONE QUARTER':
    #       print(character_name, decimal_digit_value)

    #    if unicode_1_value != '':
    #       print(character_name, unicode_1_value)

         if len(general_category) != 2:
            print(character_name, general_category)
# }}}         
