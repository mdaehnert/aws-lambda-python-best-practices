$LambdaArtifactStorage=
$StackName=python-test

aws cloudformation package \
  --template-file template.yml \
  --s3-bucket $LambdaArtifactStorage \
  --output-template-file .packaged-template.yml \
&& \
aws cloudformation deploy \
  --template-file .packaged-template.yml \
  --stack-name $StackName \
  --capabilities CAPABILITY_IAM
