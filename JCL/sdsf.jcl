//H4CKRNJE JOB (1234567),'ABC 123',CLASS=A,MSGCLASS=A,
//             MSGLEVEL=(1,1),USER=,PASSWORD=,NOTIFY=&SYSUID
//REMVLF   EXEC PGM=SDSF,COND=(0,NE),REGION=0M,PARM='++111,240'
//ISFOUT   DD SYSOUT=*
//CMDOUT   DD SYSOUT=*
//ISFIN    DD *
SET CONSOLE BATCH
SET DELAY 600
ULOG
/+D009 DISPLAY USAGE PSID(2) TYPE(PAGESET)
PRINT FILE CMDOUT
PRINT
PRINT CLOSE
/*
