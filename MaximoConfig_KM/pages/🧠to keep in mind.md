filters:: {"🈳template inventory" false, "🧭topic inventory" false}

- # List of Items Not yet Embedded In Mind
- {{query (and [[🧠to keep in mind]] (property :embedded-in-mind "no") (property :keep-until-date) (not (page [[🈳Template Inventory]])))}}
  query-table:: true
  query-properties:: [:block :keep-until-date :embedded-in-mind]
  query-sort-by:: keep-until-date
  query-sort-desc:: false
-
-
-
-
-
-