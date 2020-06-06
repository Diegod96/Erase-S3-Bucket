import boto3


def delete_scraper_bucket():
    """
    Erase contents in my diegos-reddit-bucket S3 bucket
    """
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("diegos-reddit-bucket")
    bucket.objects.all().delete()


def erase_comprehend_bucket():
    """
    Erase contents in my lambda-comprehend-sent-diego S3 bucket
    """
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("lambda-comprehend-sent-diego")
    bucket.objects.all().delete()



if __name__ == '__main__':
    print("Starting to erase contents in diegos-reddit-bucket...")
    delete_scraper_bucket()
    print("Erased contents in diegos-reddit-bucket!")

    print("Starting to erase contents in lambda-comprehend-sent-diego...")
    erase_comprehend_bucket()
    print("Erased contents in lambda-comprehend-sent-diego!")
