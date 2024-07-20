# Pagination Project

This project demonstrates various pagination techniques for handling datasets. The implementation includes basic pagination, hypermedia pagination, and deletion-resilient hypermedia pagination.

## Overview

The project implements pagination techniques for efficiently navigating large datasets. It includes:

1. **Simple Pagination**: Basic pagination that retrieves a specific page of data.
2. **Hypermedia Pagination**: Enhances pagination with additional metadata like next and previous page information.
3. **Deletion-Resilient Hypermedia Pagination**: Handles dataset deletions gracefully, ensuring that page indices remain consistent.

## Files

- `1-simple_pagination.py`: Implements basic pagination.
- `2-hypermedia_pagination.py`: Adds hypermedia pagination with metadata.
- `3-hypermedia_del_pagination.py`: Implements deletion-resilient hypermedia pagination.
- `Popular_Baby_Names.csv`: Dataset used for pagination.
- `1-main.py`: Script to test basic pagination.
- `2-main.py`: Script to test hypermedia pagination.
- `3-main.py`: Script to test deletion-resilient hypermedia pagination.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-repository-folder
