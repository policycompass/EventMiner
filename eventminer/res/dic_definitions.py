"""
Central definitions for Event-Mining.
"""


dic_definitions = {
    "day_range": range(1, 32),
    "days": {"1st": "1",
             "2nd": "2",
             "3rd": "3",
             "4th": "4",
             "5th": "5",
             "6th": "6",
             "7th": "7",
             "8th": "8",
             "9th": "9",
             "10th": "10",
             "11th": "11",
             "12th": "12",
             "13th": "13",
             "14th": "14",
             "15th": "15",
             "16th": "16",
             "17th": "17",
             "18th": "18",
             "19th": "19",
             "20th": "20",
             "21st": "21",
             "22nd": "22",
             "23rd": "23",
             "24th": "24",
             "25th": "25",
             "26th": "26",
             "27th": "27",
             "28th": "28",
             "29th": "29",
             "30th": "30",
             "31st": "31"
             },
    "months": {"january": "1",
               "february": "2",
               "march": "3",
               "april": "4",
               "may": "5",
               "june": "6",
               "july": "7",
               "august": "8",
               "september": "9",
               "october": "10",
               "november": "11",
               "december": "12"
               },
    "year_range": range(32, 2300),
    "seasons": ["spring", "summer", "autumn", "winter"],
    "keywords_year": ["after", "before", "by", "in", "since"],
    "keywords_time_span": ["and", "to", "until", "-"],
    "exclusion_tags": ["NNP-ORG"]

}