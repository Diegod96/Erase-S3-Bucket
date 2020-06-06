import boto3


def delete_scraper_bucket():
    """
    Erase contents in my diegos-reddit-bucket S3 bucket
    """
    s3 = boto3.client("s3")
    bucket_name = "diegos-reddit-bucket"
    comments = "comments"
    articles = "articles"
    complete = "complete.txt"

    print("Clearing comments folder...")
    s3.delete_object(Bucket=bucket_name, Key=comments)
    print("Cleared comments folder!")

    print("Cleared articles folder...")
    s3.delete_object(Bucket=bucket_name, Key=articles)
    print("Cleared articles folder!")

    print("Deleting complete.txt...")
    s3.delete_object(Bucket=bucket_name, Key=complete)
    print("complete.txt deleted!")


def erase_comprehend_bucket():
    """
    Erase contents in my lambda-comprehend-sent-diego S3 bucket
    """
    s3 = boto3.client("s3")
    bucket_name = "lambda-comprehend-sent-diego"
    done = "done"
    blob = "blob.txt"

    print("Clearing done folder...")
    s3.delete_object(Bucket=bucket_name, Key=done)
    print("Cleared done folder!")

    print("Deleting blob.txt...")
    s3.delete_object(Bucket=bucket_name, Key=blob)
    print("blob.txt deleted!")



if __name__ == '__main__':
    print("Starting to erase contents in diegos-reddit-bucket...")
    delete_scraper_bucket()
    print("Erased contents in diegos-reddit-bucket!")

    print("Starting to erase contents in lambda-comprehend-sent-diego...")
    erase_comprehend_bucket()
    print("Erased contents in lambda-comprehend-sent-diego!")
