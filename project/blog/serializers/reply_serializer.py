from rest_framework import serializers
from db.models.reply import Reply


class ReplySerializers(serializers.ModelSerializer):
    
    
    class Meta:
        model = Reply
        fields = [ 'id', 'comment_id','reply','created_at','updated_at']



