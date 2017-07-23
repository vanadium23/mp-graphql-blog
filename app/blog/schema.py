import graphene

from graphene_django.types import DjangoObjectType

from blog.models import User, Post, Comment


class UserType(DjangoObjectType):
    class Meta:
        model = User


class PostType(DjangoObjectType):
    '''Post model to fetch with GraphQL'''

    class Meta:
        model = Post


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int(required=True))
    me = graphene.Field(UserType)

    def resolve_post(self, args, context, info):
        return Post.objects.prefetch_related('comments').get(pk=args['id'])

    def resolve_me(self, args, context, info):
        return User.objects.get(id=1)


schema = graphene.Schema(query=Query)
