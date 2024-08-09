# Introduction
This folder is a document about the architecture chosen to make the project. 

## API Service structure:

```bash
.
├── cmd
├── external
│   ├── db
│   ├── logger
│   └── strings
├── internal
│   ├── adapters
│   │   └── rpc
│   ├── core
│   │   ├── application
│   │   ├── domain
│   │   │   ├── entity
│   │   │   │   ├── dto
│   │   │   │   └── valueObject
│   │   │   ├── useCase
│   │   │   └── rpc
│   │   └── useCase
│   └── handler
│       └── http
└── product_api_proto
```
