from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from teams.models import Team
from django.forms.models import model_to_dict


class TeamView(APIView):
    def post(self, request: Request):
        team_data = request.data
        team = Team.objects.create(
            name=team_data["name"],
            titles=team_data["titles"],
            top_scorer=team_data["top_scorer"],
            fifa_code=team_data["fifa_code"],
            founded_at=team_data["founded_at"]
        )
        return Response(model_to_dict(team), status.HTTP_201_CREATED)

    def get(self, request: Request):
        teams = Team.objects.all()
        teams_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)
        return Response(teams_list, status.HTTP_200_OK)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND
            )
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND
            )

        for key, value in request.data.items():
            setattr(team, key, value)
        team.save()
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND
            )

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
