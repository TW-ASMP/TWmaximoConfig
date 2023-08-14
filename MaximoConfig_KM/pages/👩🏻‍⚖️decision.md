filters:: {"🈳template inventory" false, "🧭topic inventory" false}

-
- # All Tentative Decisions
- {{query (and [[👩🏻‍⚖️decision]] (property :tentative "yes") (not (page [[🈳Template Inventory]])))(and [[👩🏻‍⚖️decision]] (property :tentative "yes") (not))(and [[👩🏻‍⚖️decision]] (property :tentative "yes"))[[👩🏻‍⚖️decision]]}}
  query-table:: true
  query-properties:: [:block :initiative :tentative]