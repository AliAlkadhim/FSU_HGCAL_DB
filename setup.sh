#!/bin/bash

chmod -R 777 *
###export PATH=./:$PATH
### it's already in PYTHONPATH from the lcd setup.sh
############ Source the lcd setup
export ROOT_SOURCE="/software/ROOT_6_06_06/bin/thisroot.sh";
export HEXPLOT_DIR="/software/hexplot/bin";
export WORKFLOW_DIR="/home/workflow/lcd_hgcal_analysisworkflows-v0.6";
export DB_DIR="$WORKFLOW_DIR/database/csv";

export PYTHONPATH=$WORKFLOW_DIR:$PYTHONPATH;

export TMPFILES_DIR_IV="/home/output/hgsensor_iv"
export SUMMARY_DIR_IV="/home/output/summaryhgsensor_iv"
source $WORKFLOW_DIR/workflow_IV/setup.sh;

export TMPFILES_DIR_CV="/home/output/hgsensor_cv"
export SUMMARY_DIR_CV="/home/output/summaryhgsensor_cv" 
source $WORKFLOW_DIR/workflow_CV/setup.sh;

######Add input directory

export INPUT_DIR="/home/input/"











# Below is the exports when I work on it on my own docker of lcd_analysis_workflows on my ububtu machine
# export ROOT_SOURCE="/software/ROOT_6_06_06/bin/thisroot.sh";

# export HEXPLOT_DIR="/software/hexplot/bin";

# export WORKFLOW_DIR="/home/lcd_hgcal_analysisworkflows";

# export DB_DIR="$WORKFLOW_DIR/database/csv";

# export PYTHONPATH=$WORKFLOW_DIR:$PYTHONPATH;

# export TMPFILES_DIR_IV="/home/OUTPUT_ALI/TMPFILES_DIR_IV"

# export SUMMARY_DIR_IV="/home/OUTPUT_ALI/SUMMARY_DIR_IV"

# source $WORKFLOW_DIR/workflow_IV/setup.sh;

# export TMPFILES_DIR_CV="/home/OUTPUT_ALI/TMPFILES_DIR_CV"

# export SUMMARY_DIR_CV="/home/OUTPUT_ALI/SUMMARY_DIR_CV"

# source $WORKFLOW_DIR/workflow_CV/setup.sh;
