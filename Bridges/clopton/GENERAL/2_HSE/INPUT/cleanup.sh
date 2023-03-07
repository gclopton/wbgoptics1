#!/bin/bash

if [ -f "INCAR_final" ] && [ -f "INCAR_updated" ] && [ -f "INCAR" ]; then
    rm -f "INCAR" "INCAR_updated"  # Delete old files if they exist
    mv "INCAR_final" "INCAR"  # Rename the final file to INCAR
    echo "Successfully renamed INCAR_final to INCAR"
else
    echo "INCAR_final, INCAR_updated, or INCAR does not exist in the current directory"
fi
