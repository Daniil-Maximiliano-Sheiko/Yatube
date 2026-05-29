from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, following):
        request = self.context.get('request')
        if request and request.user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        return following

    def validate(self, data):
        request = self.context.get('request')
        following = data.get('following')
        if (
            request
            and following
            and Follow.objects.filter(
                user=request.user,
                following=following
            ).exists()
        ):
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя.'
            )
        return data
