@echo off

copy git/pre-commit .git/hooks
copy git/pre-push .git/hooks

PAUSE