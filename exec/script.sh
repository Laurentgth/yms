# Validate passed reference
reference=$1
if [ -z $reference ]
then
    echo "YMS error - You must pass a video's locator"
    exit 1
fi


# Trim passed reference
URL_slug_1="https://youtu.be/"
URL_slug_2="https://youtube.com/"
URL_slug_3="https://www.youtube.com/watch?v="
URL_slug_4="shorts/"
URL_slug_5="?feature=share"
URL_slug_6="&feature=share"
passed_id=`
    echo "$reference" |\
    sed -e "s#^$URL_slug_1##" |\
    sed -e "s#^$URL_slug_2##" |\
    sed -e "s#^$URL_slug_3##" |\
    sed -e "s#^$URL_slug_4##" |\
    sed -e "s#$URL_slug_5##" |\
    sed -e "s#$URL_slug_6##"  \
`


# Build URL to access
base_URL="https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails"
vid_id=$passed_id
api_key=`cat exec/api.key`
request_URL="$base_URL&key=$api_key&id=$vid_id"


# Perform HTTPS request, process and store it, result in clipboard (Mac OS)
result=`curl -s $request_URL --header 'Accept: application/json' --compressed | python3.9 exec/python-scripts/api-result-controller.py`


# Return result in clipboard and stdout
echo $result | pbcopy
echo $result
echo "-> Copied to clipboard!"
