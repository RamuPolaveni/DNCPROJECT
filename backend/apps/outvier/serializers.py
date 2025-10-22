from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    PersonalProfile, Goal, GoalMilestone, TeamMatch, 
    GrowthPathway, PathwayStep, LearningProgress, Achievement,
    LearningStreak, ProgressInsight, Notification, NotificationPreference,
    NotificationSchedule
)
from apps.users.models import Skill
from apps.projects.models import Project, ProjectCategory

User = get_user_model()


class PersonalProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = PersonalProfile
        fields = [
            'id', 'user', 'user_name', 'user_email',
            'personality_type', 'communication_style', 'work_preference',
            'strengths', 'weaknesses', 'opportunities', 'growth_areas',
            'leadership_score', 'technical_score', 'creativity_score', 'collaboration_score',
            'is_complete', 'last_updated', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'last_updated']


class GoalMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalMilestone
        fields = [
            'id', 'title', 'description', 'target_date', 
            'completed_date', 'is_completed', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class GoalSerializer(serializers.ModelSerializer):
    milestones = GoalMilestoneSerializer(many=True, read_only=True)
    related_skills_names = serializers.StringRelatedField(
        source='related_skills', many=True, read_only=True
    )
    related_project_title = serializers.CharField(
        source='related_project.title', read_only=True
    )
    related_pathway_title = serializers.CharField(
        source='related_pathway.title', read_only=True
    )
    days_remaining = serializers.SerializerMethodField()
    is_overdue = serializers.SerializerMethodField()
    progress_status = serializers.SerializerMethodField()
    
    class Meta:
        model = Goal
        fields = [
            'id', 'user', 'title', 'description', 'goal_type', 'priority', 'status',
            'start_date', 'target_date', 'completed_date', 'progress_percentage',
            'is_completed', 'related_skills', 'related_skills_names',
            'related_project', 'related_project_title', 'related_pathway', 'related_pathway_title',
            'milestones', 'days_remaining', 'is_overdue', 'progress_status',
            'target_value', 'current_value', 'unit', 'is_public', 'allow_mentorship',
            'reminder_frequency', 'time_spent', 'last_activity', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'last_activity']
    
    def get_days_remaining(self, obj):
        return obj.days_remaining
    
    def get_is_overdue(self, obj):
        return obj.is_overdue
    
    def get_progress_status(self, obj):
        return obj.progress_status
    
    def validate(self, data):
        """Validate goal data"""
        start_date = data.get('start_date')
        target_date = data.get('target_date')
        
        if start_date and target_date and start_date > target_date:
            raise serializers.ValidationError("Start date cannot be after target date")
        
        return data


class TeamMatchSerializer(serializers.ModelSerializer):
    matched_users_names = serializers.StringRelatedField(
        source='matched_users', many=True, read_only=True
    )
    required_skills_names = serializers.StringRelatedField(
        source='required_skills', many=True, read_only=True
    )
    project_categories_names = serializers.StringRelatedField(
        source='project_categories', many=True, read_only=True
    )
    
    class Meta:
        model = TeamMatch
        fields = [
            'id', 'user', 'match_type', 'matched_users', 'matched_users_names',
            'required_skills', 'required_skills_names', 'preferred_roles',
            'project_categories', 'project_categories_names', 'compatibility_score',
            'is_active', 'is_accepted', 'accepted_at', 'match_reason',
            'suggested_roles', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class PathwayStepSerializer(serializers.ModelSerializer):
    prerequisites_titles = serializers.StringRelatedField(
        source='prerequisites', many=True, read_only=True
    )
    
    class Meta:
        model = PathwayStep
        fields = [
            'id', 'pathway', 'step_number', 'title', 'description', 'step_type',
            'content_url', 'estimated_duration', 'prerequisites', 'prerequisites_titles',
            'is_completed', 'completed_at', 'completion_notes', 'has_quiz',
            'passing_score', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class LearningProgressSerializer(serializers.ModelSerializer):
    pathway_step_title = serializers.CharField(
        source='pathway_step.title', read_only=True
    )
    
    class Meta:
        model = LearningProgress
        fields = [
            'id', 'user', 'pathway_step', 'pathway_step_title', 'started_at',
            'completed_at', 'time_spent', 'quiz_score', 'quiz_attempts',
            'difficulty_rating', 'helpfulness_rating', 'notes'
        ]
        read_only_fields = ['id', 'started_at']


class AchievementSerializer(serializers.ModelSerializer):
    related_goal_title = serializers.CharField(
        source='related_goal.title', read_only=True
    )
    related_pathway_title = serializers.CharField(
        source='related_pathway.title', read_only=True
    )
    
    class Meta:
        model = Achievement
        fields = [
            'id', 'user', 'achievement_type', 'title', 'description', 'icon_name',
            'related_goal', 'related_goal_title', 'related_pathway', 'related_pathway_title',
            'points_earned', 'is_unlocked', 'unlocked_at', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class LearningStreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningStreak
        fields = [
            'id', 'user', 'current_streak', 'longest_streak', 'last_activity_date',
            'target_streak', 'streak_goal_achieved', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class GrowthPathwaySerializer(serializers.ModelSerializer):
    required_skills_names = serializers.StringRelatedField(
        source='required_skills', many=True, read_only=True
    )
    recommended_projects_titles = serializers.StringRelatedField(
        source='recommended_projects', many=True, read_only=True
    )
    progress_percentage = serializers.SerializerMethodField()
    estimated_completion_date = serializers.SerializerMethodField()
    learning_velocity = serializers.SerializerMethodField()
    steps = PathwayStepSerializer(many=True, read_only=True)
    
    class Meta:
        model = GrowthPathway
        fields = [
            'id', 'user', 'title', 'description', 'pathway_type', 'difficulty_level', 'status',
            'required_skills', 'required_skills_names', 'recommended_projects',
            'recommended_projects_titles', 'learning_resources', 'current_step',
            'total_steps', 'progress_percentage', 'is_completed', 'completed_at',
            'estimated_duration', 'is_public', 'allow_collaboration', 'total_time_spent',
            'last_activity', 'completion_rate', 'preferred_learning_style',
            'estimated_completion_date', 'learning_velocity', 'steps',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'last_activity']
    
    def get_progress_percentage(self, obj):
        return obj.progress_percentage
    
    def get_estimated_completion_date(self, obj):
        return obj.estimated_completion_date
    
    def get_learning_velocity(self, obj):
        return obj.learning_velocity


class ProgressInsightSerializer(serializers.ModelSerializer):
    related_goal_title = serializers.CharField(
        source='related_goal.title', read_only=True
    )
    related_pathway_title = serializers.CharField(
        source='related_pathway.title', read_only=True
    )
    
    class Meta:
        model = ProgressInsight
        fields = [
            'id', 'user', 'insight_type', 'title', 'message',
            'related_goal', 'related_goal_title', 'related_match',
            'related_pathway', 'related_pathway_title', 'confidence_score',
            'is_positive', 'is_read', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class UserDashboardSerializer(serializers.ModelSerializer):
    """Comprehensive dashboard data for Outvier mobile app"""
    profile = PersonalProfileSerializer(read_only=True)
    active_goals = serializers.SerializerMethodField()
    recent_matches = serializers.SerializerMethodField()
    current_pathways = serializers.SerializerMethodField()
    recent_insights = serializers.SerializerMethodField()
    progress_summary = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'role',
            'profile', 'active_goals', 'recent_matches', 'current_pathways',
            'recent_insights', 'progress_summary'
        ]
    
    def get_active_goals(self, obj):
        active_goals = obj.outvier_goals.filter(is_completed=False)[:5]
        return GoalSerializer(active_goals, many=True).data
    
    def get_recent_matches(self, obj):
        recent_matches = obj.outvier_matches.filter(is_active=True)[:5]
        return TeamMatchSerializer(recent_matches, many=True).data
    
    def get_current_pathways(self, obj):
        current_pathways = obj.outvier_pathways.filter(is_completed=False)[:3]
        return GrowthPathwaySerializer(current_pathways, many=True).data
    
    def get_recent_insights(self, obj):
        recent_insights = obj.outvier_insights.filter(is_read=False)[:5]
        return ProgressInsightSerializer(recent_insights, many=True).data
    
    def get_progress_summary(self, obj):
        goals = obj.outvier_goals.all()
        total_goals = goals.count()
        completed_goals = goals.filter(is_completed=True).count()
        
        pathways = obj.outvier_pathways.all()
        total_pathways = pathways.count()
        completed_pathways = pathways.filter(is_completed=True).count()
        
        return {
            'total_goals': total_goals,
            'completed_goals': completed_goals,
            'goal_completion_rate': (completed_goals / total_goals * 100) if total_goals > 0 else 0,
            'total_pathways': total_pathways,
            'completed_pathways': completed_pathways,
            'pathway_completion_rate': (completed_pathways / total_pathways * 100) if total_pathways > 0 else 0,
        }


class NotificationSerializer(serializers.ModelSerializer):
    related_goal_title = serializers.CharField(
        source='related_goal.title', read_only=True
    )
    related_pathway_title = serializers.CharField(
        source='related_pathway.title', read_only=True
    )
    related_achievement_title = serializers.CharField(
        source='related_achievement.title', read_only=True
    )
    
    class Meta:
        model = Notification
        fields = [
            'id', 'user', 'notification_type', 'title', 'message', 'priority',
            'related_goal', 'related_goal_title', 'related_pathway', 'related_pathway_title',
            'related_achievement', 'related_achievement_title', 'related_match',
            'is_read', 'is_sent', 'sent_at', 'action_url', 'action_text',
            'scheduled_for', 'expires_at', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class NotificationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPreference
        fields = [
            'id', 'user', 'goal_reminders', 'goal_deadlines', 'goal_milestones',
            'pathway_reminders', 'pathway_steps', 'achievements', 'streak_reminders',
            'streak_broken', 'matches', 'insights', 'system_updates',
            'email_notifications', 'push_notifications', 'in_app_notifications',
            'quiet_hours_start', 'quiet_hours_end', 'timezone', 'reminder_frequency',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class NotificationScheduleSerializer(serializers.ModelSerializer):
    related_goal_title = serializers.CharField(
        source='related_goal.title', read_only=True
    )
    related_pathway_title = serializers.CharField(
        source='related_pathway.title', read_only=True
    )
    
    class Meta:
        model = NotificationSchedule
        fields = [
            'id', 'user', 'notification_type', 'title_template', 'message_template',
            'frequency', 'time_of_day', 'days_of_week', 'days_of_month',
            'is_active', 'start_date', 'end_date', 'related_goal', 'related_goal_title',
            'related_pathway', 'related_pathway_title', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
