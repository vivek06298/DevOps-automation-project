#!/bin/bash
set -e

read -p "Enter new branch name: " branch_name
git checkout -b "$branch_name"

git add .

read -p "Enter commit message: " commit_message
git commit -m "$commit_message"

git push -u origin "$branch_name"

echo "Branch created, committed, and pushed successfully."