from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # custom serializer methods 
    len_name = serializers.SerializerMethodField()
  
    class Meta:
        model = Movie
        fields = '__all__'
        # fields =['name','id','description']
        # exclude = ['name']
  
    
    def get_len_name(self,object):
        return f"name count :{len(object.name)}"
        
    # validatrs_function :
    def name_length(x):
        if len(x) <2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return x
        # Object-level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("The name cannot be the same as the description.")
        return data





# # validatrs_function :
# def name_length(x):
#     if len(x) <2:
#         raise serializers.ValidationError("Name must be at least 2 characters long.")
#     return x

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators =[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # Object-level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("The name cannot be the same as the description.")
#         return data

#     # Field-level validation
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name must be at least 2 characters long.")
#     #     return value
