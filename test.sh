#!/bin/bash

# Run 'fedpkg local' first

cd dhcp-4.2.2/tests
make check

cd ../common/tests
make test_alloc
./test_alloc
