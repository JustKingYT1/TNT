from server.routers import staff, users_staff, users_viewer, viewers, tv_channels, schedules, equipment_sets, staff_teams, times, shows

routs = (users_staff.user_staff_router, staff.staff_router, users_viewer.user_viewer_router, viewers.viewers_router, tv_channels.channel_router)
