```mermaid
flowchart TD
    subgraph SUT_Input [Stage 1: SUT Specification]
        A1[Đặc tả API] --> B[Spec & Schema Parser]
        A2[Business Rule từ FR-01 đến FR-19] --> C[Domain & Rule Extractor]
        A3[Security matrix SEC-01 đến SEC-07] --> C
    end

    subgraph Agent_Core [Stage 2: AI Test Generator Engine]
        B --> D[Xác nhận context và constraint]
        C --> D
        D --> F1[Sinh test case Partition và BVA]
        D --> F2[Sinh test case State transition]
        D --> F3[Sinh test case Security & Injection]
        D --> F4[Sinh test case schema]
    end

    subgraph Post_Processing [Stage 3: Synthesis & Verification]
        F1 & F2 & F3 & F4 --> G[Tổng hợp và & Khử trùng lắp]
        G --> H[Con người kiểm tra]
        H --> I{Hợp lệ?}
        I -- Không --> E[Giữ lại để audit]
        I -- Có --> J[Đưa lên postman/newman]
    end

    subgraph Execution [Stage 4: Execution & Reporting]
        J --> K[Gắn student ID trong pre-request script]
        K --> L[Thực thi test case trên newman hoặc postman GUI]
        L --> M[Sinh HTML / JSON Test Reports]
        L --> N[Báo cáo lỗi trên GitHub issues]
    end
```

* Các bước thực hiện
    - Đọc các đặc tả của hệ thống
    - AI thực hiện sinh ra những test case dựa trên đặc tả được đưa (bao gồm Partiton, Security, State, Schema)
    - Các test case được sinh ra sẽ được người dùng kiểm tra lại trước khi đưa lên Postman/Newman
    - Người dùng thực hiện các test case, sinh test report, báo cáo lỗi trên github issues