
flowchart TD
    Start([Start: generate_api_tests]) --> LoadSpec[Load Markdown Spec<br/><code>load_markdown_spec(api_spec_path)</code>]
    LoadSpec --> ExtractContract[Extract Endpoint Contract<br/><code>extract_endpoint(spec_data, target_endpoint)</code>]
    ExtractContract --> InitList[Initialize <code>test_cases = []</code>]

    %% 1. Domain Partitions Loop
    InitList --> LoopParams{For each parameter<br/>in endpoint_contract.parameters}
    LoopParams -- Yes --> GenPartitions[Generate Boundary Partitions<br/><code>generate_boundary_partitions(param)</code>]
    GenPartitions --> AppendPartitions[Extend <code>test_cases</code>]
    AppendPartitions --> LoopParams
    LoopParams -- Nflowchart TD
    Start([Start: generate_api_tests]) --> LoadSpec[Load Markdown Spec<br/><code>load_markdown_spec(api_spec_path)</code>]
    LoadSpec --> ExtractContract[Extract Endpoint Contract<br/><code>extract_endpoint(spec_data, target_endpoint)</code>]
    ExtractContract flowchart TD
    Start([Start: generate_api_tests]) --> LoadSpec[Load Markdown Spec<br/><code>load_markdown_spec(api_spec_path)</code>]
    LoadSpec --> ExtractContract[Extract Endpoint Contract<br/><code>extract_endpoint(spec_data, target_endpoint)</code>]
    ExtractContract --> InitList[Initialize <code>test_cases = []</code>]

    %% 1. Domain Partitions Loop
    InitList --> LoopParams{For each parameter<br/>in endpoint_contract.parameters}
    LoopParams -- Yes --> GenPartitions[Generate Boundary Partitions<br/><code>generate_boundary_partitions(param)</code>]
    GenPartitions --> AppendPartitions[Extend <code>test_cases</code>]
    AppendPartitions --> LoopParams
    LoopParams -- No --> CheckState{endpoint_contract.affects_state?}

    %% 2. State Transitions Condition
    CheckState -- Yes --> GenState[Generate State Transition Matrix<br/><code>generate_state_transition_matrix(...)</code>]
    GenState --> AppendState[Extend <code>test_cases</code>]
    AppendState --> GenSecurity
    CheckState -- No --> GenSecurity

    %% 3. Security Requirements
    GenSecurity[Generate Security Payloads<br/><code>generate_security_payloads(...)</code>] --> AppendSecurity[Extend <code>test_cases</code>]

    %% 4. Schema Validation
    AppendSecurity --> GenSchema[Generate Schema Validation Test<br/><code>generate_schema_validation_test(...)</code>]
    GenSchema --> AppendSchema[Append to <code>test_cases</code>]

    %% Final Output
    AppendSchema --> FormatOutput[Format to Excel & Postman Collection<br/><code>format_to_excel_and_collection(test_cases)</code>]
    FormatOutput --> End([End: Return Result])--> InitList[Initialize <code>test_cases = []</code>]

    %% 1. Domain Partitions Loop
    InitList --> LoopParams{For each parameter<br/>in endpoint_contract.parameters}
    LoopParams -- Yes --> GenPartitions[Generate Boundary Partitions<br/><code>generate_boundary_partitions(param)</code>]
    GenPartitions --> AppendPartitions[Extend <code>test_cases</code>]
    AppendPartitions --> LoopParams
    LoopParams -- No --> CheckState{endpoint_contract.affects_state?}

    %% 2. State Transitions Condition
    CheckState -- Yes --> GenState[Generate State Transition Matrix<br/><code>generate_state_transition_matrix(...)</code>]
    GenState --> AppendState[Extend <code>test_cases</code>]
    AppendState --> GenSecurity
    CheckState -- No --> GenSecurity

    %% 3. Security Requirements
    GenSecurity[Generate Security Payloads<br/><code>generate_security_payloads(...)</code>] --> AppendSecurity[Extend <code>test_cases</code>]

    %% 4. Schema Validation
    AppendSecurity --> GenSchema[Generate Schema Validation Test<br/><code>generate_schema_validation_test(...)</code>]
    GenSchema --> AppendSchema[Append to <code>test_cases</code>]

    %% Final Output
    AppendSchema --> FormatOutput[Format to Excel & Postman Collection<br/><code>format_to_excel_and_collection(test_cases)</code>]
    FormatOutput --> End([End: Return Result]) --> CheckState{endpoint_contract.affects_state?}

    %% 2. State Transitions Condition
    CheckState -- Yes --> GenState[Generate State Transition Matrix<br/><code>generate_state_transition_matrix(...)</code>]
    GenState --> AppendState[Extend <code>test_cases</code>]
    AppendState --> GenSecurity
    CheckState -- No --> GenSecurity

    %% 3. Security Requirements
    GenSecurity[Generate Security Payloads<br/><code>generate_security_payloads(...)</code>] --> AppendSecurity[Extend <code>test_cases</code>]

    %% 4. Schema Validation
    AppendSecurity --> GenSchema[Generate Schema Validation Test<br/><code>generate_schema_validation_test(...)</code>]
    GenSchema --> AppendSchema[Append to <code>test_cases</code>]

    %% Final Output
    AppendSchema --> FormatOutput[Format to Excel & Postman Collection<br/><code>format_to_excel_and_collection(test_cases)</code>]
    FormatOutput --> End([End: Return Result])