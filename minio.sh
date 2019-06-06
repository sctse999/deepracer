docker run --rm -p 9000:9000 --name minio1 \
  --network=sagemaker-local \
  -e "MINIO_ACCESS_KEY=minio" \
  -e "MINIO_SECRET_KEY=miniokey" \
  -v /tmp/data:/data \
  minio/minio server /data


# export MINIO_ACCESS_KEY=minio
# export MINIO_SECRET_KEY=miniokey

# minio server minio