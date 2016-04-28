% main control code - assumes full state knowledge
%
%
% Modified: 
%   2/11/2014 - R. Beard
%   2/18/2014 - R. Beard
%   2/24/2014 - R. Beard
%

function v_c=controller_home_full_state(uu,P)

    % process inputs to function
    % robots - own team
    for i=1:P.num_robots,
        robot(:,i)   = uu(1+3*(i-1):3+3*(i-1));
    end
    NN = 3*P.num_robots;
    % robots - opponent
    for i=1:P.num_robots,
        opponent(:,i)   = uu(1+3*(i-1)+NN:3+3*(i-1)+NN);
    end
    NN = NN + 3*P.num_robots;
    % ball
    ball = [uu(1+NN); uu(2+NN)];
    NN = NN + 2;
    % score: own team is score(1), opponent is score(2)
    score = [uu(1+NN); uu(2+NN)];
    NN = NN + 2;
    % current time
    t      = uu(1+NN);

% original
%     robot #1 positions itself behind ball and rushes the goal.
%     v1 = play_rush_goal(robot(:,1), ball, P);
%     v1 = skill_follow_ball_on_line(robot(:,1), ball, -1*P.field_width/3, P);
%     v1 = play_get_behind_ball(robot(:,1), ball, P);
%     robot #2 stays on line, following the ball, facing the goal
%     v2 = skill_follow_ball_on_line(robot(:,2), ball, -2*P.field_width/3, P);
%     v2 = play_rush_goal(robot(:,2), ball, P);

    
%     v1 = skill_spin_ccw(robot(:,1),0.1, P);
%     v2 = skill_spin_cw(robot(:,2),0.01, P);

%     temp = play_face_each_other(robot(:,1), robot(:,2), P);
%     v1 = temp(1:3);
%     v2 = temp(4:6);
    
%     temp = strategy_split_field(robot(:,1), robot(:,2), ball, P);
%     v1 = temp(1:3);
%     v2 = temp(4:6);


if ball(1) < 0,         % activate defense
    temp = strategy_sweeper_keeper(robot(:,1), robot(:,2), ball, P);
    v1 = temp(1:3);
    v2 = temp(4:6);
else                    %activate offense
    temp = strategy_defensive_midfielder(robot(:,1), robot(:,2), ball, P);
    v1 = temp(1:3);
    v2 = temp(4:6);
end

    % output velocity commands to robots
    v1 = utility_saturate_velocity(v1,P);
    v2 = utility_saturate_velocity(v2,P);
    v_c = [v1; v2];
end

%---------------------------------------------------------------------------
% STRATEGIES!!!!!!!
%---------------------------------------------------------------------------

%-----------------------------------------
% strategy - one goalee and one sweeper
% Robot1 tries to block the ball at the goal, Robot2 plays sweeper in the
% entire defensive half
function v=strategy_sweeper_keeper(robot1, robot2, ball, P)

% normal vector from ball to goal
n = P.goal-ball;
n = n/norm(n);
% compute position 10cm behind ball, but aligned with goal.
position = ball - 0.2*n;

v1 = play_get_behind_ball(robot1, ball, P);

if ball(1) > -P.field_length/6,
    v2 = skill_follow_ball_on_line(robot2, ball, -P.field_length/4, P);
else
    v2 = play_get_behind_ball(robot2, ball, P);
end

v = [v1; v2];
end

%-----------------------------------------
% strategy - one striker and one defensive midfielder
% Robot1 tries to score, Robot2 stays to block the counter attack
function v=strategy_defensive_midfielder(robot1, robot2, ball, P)

% normal vector from ball to goal
n = P.goal-ball;
n = n/norm(n);
% compute position 10cm behind ball, but aligned with goal.
position = ball - 0.2*n;

v1 = play_get_behind_ball(robot1, ball, P);

if ball(1) > P.field_length/4,
    v2 = skill_follow_ball_on_line(robot2, ball, P.field_length/6, P);
else
    v2 = play_get_behind_ball(robot2, ball, P);
end

v = [v1; v2];
end

%-----------------------------------------
% strategy - both robots rush goals
% Robot1 stays in the top 75% of the field and Robot 2 stays in the bottom 75%
function v=strategy_split_field(robot1, robot2, ball, P)

% normal vector from ball to goal
n = P.goal-ball;
n = n/norm(n);
% compute position 10cm behind ball, but aligned with goal.
position = ball - 0.2*n;

temp = position;

if norm(position-robot1(1:2))<.21,
    v1 = skill_go_to_point(robot1, P.goal, P);
else
    if position(2) <= -P.field_width/4,
       temp(2) = -P.field_width/4;
    end
    v1 = skill_go_to_point(robot1, temp, P);
end

if norm(position-robot2(1:2))<.21,
    v2 = skill_go_to_point(robot2, P.goal, P);
else
    if position(2) >= P.field_width/4,
        position(2) = P.field_width/4;
    end
    v2 = skill_go_to_point(robot2, position, P);
end
v = [v1; v2];
end


%---------------------------------------------------------------------------
% PLAYS!!!!!!!
%---------------------------------------------------------------------------


function v=play_get_behind_ball(robot, ball, P)
  % normal vector from ball to goal
  n = P.goal-ball;
  n = n/norm(n);
  % compute position 10cm behind ball, but aligned with goal.
  position = ball - 0.2*n;
  
  if ball(1) > robot(1)
      v = play_rush_goal(robot, ball, P);
  else
      if ball(2) >= robot(2)
          position(1) = position(1)-0.1;
          position(2) = position(2)-0.1;
          v = skill_go_to_point(robot, position, P);
      else
          position(1) = position(1)-0.1;          
          position(2) = position(2)+0.1;
          v = skill_go_to_point(robot, position, P);
      end
  end
  
end

%-----------------------------------------
% play - face each other
function v=play_face_each_other(robot1, robot2, P)
    
    v1 = play_face_teammate(robot1, robot2, P);
    v2 = play_face_teammate(robot2, robot1, P);
    
    v = [v1; v2];
end


%-----------------------------------------
% play - face teammate
% robot1 rotates toward robot2
function v=play_face_teammate(robot1, robot2, P)
    
    vx = 0;
    vy = 0;

    % control angle to -pi/2
    theta_d = atan2(robot2(2)-robot1(2), robot2(1)-robot1(1));
    omega = -P.control_k_phi*(robot1(3) - theta_d); 
    
    v = [vx; vy; omega];
end


%-----------------------------------------
% play - rush goal
%   - go to position behind ball
%   - if ball is between robot and goal, go to goal
% NOTE:  This is a play because it is built on skills, and not control
% commands.  Skills are built on control commands.  A strategy would employ
% plays at a lower level.  For example, switching between offense and
% defense would be a strategy.
function v = play_rush_goal(robot, ball, P)
  
  % normal vector from ball to goal
  n = P.goal-ball;
  n = n/norm(n);
  % compute position 10cm behind ball, but aligned with goal.
  position = ball - 0.2*n;
    
  if norm(position-robot(1:2))<.21,
      v = skill_go_to_point(robot, P.goal, P);
  else
      v = skill_go_to_point(robot, position, P);
  end
end



%---------------------------------------------------------------------------
% SKILLS !!!!!!!
%---------------------------------------------------------------------------


%-----------------------------------------
% skill - spin counter clockwise
% speed is how fast it spins. range between 0.01 - 1
function v=skill_spin_ccw(robot, speed, P)

    vx = 0;
    vy = 0;

    % control angle to -pi/2
    theta_d = robot(3)+speed*180/pi;
    omega = -P.control_k_phi*(robot(3) - theta_d); 
    
    v = [vx; vy; omega];
end

%-----------------------------------------
% skill - spin clockwise
% speed is how fast it spins. range between 0.01 - 1
function v=skill_spin_cw(robot, speed, P)

    vx = 0;
    vy = 0;

    % control angle to -pi/2
    theta_d = robot(3)-speed*180/pi;
    omega = -P.control_k_phi*(robot(3) - theta_d); 
    
    v = [vx; vy; omega];
end


%-----------------------------------------
% skill - follow ball on line
%   follows the y-position of the ball, while maintaining x-position at
%   x_pos.  Angle always faces the goal.

function v=skill_follow_ball_on_line(robot, ball, x_pos, P)
   
persistent ball_previous;    
        
    % control x position to stay on current line
    vx = -P.control_k_vx*(robot(1)-x_pos);
    
    if ball_previous - ball(2) > 0, % ball is moving down
        % control y position to match the ball's y-position
        vy = -P.control_k_vy*(robot(2)-ball(2))-0.3;
    else                            % ball is moving up
        vy = -P.control_k_vy*(robot(2)-ball(2))+0.3;
    end

    % control angle to -pi/2
    theta_d = atan2(P.goal(2)-robot(2), P.goal(1)-robot(1));
    omega = -P.control_k_phi*(robot(3) - theta_d); 
    
    ball_previous = ball(2);
   
    v = [vx; vy; omega];
end

%-----------------------------------------
% skill - go to point
%   follows the y-position of the ball, while maintaining x-position at
%   x_pos.  Angle always faces the goal.

function v=skill_go_to_point(robot, point, P)

    % control x position to stay on current line
    vx = -P.control_k_vx*(robot(1)-point(1));
    
    % control y position to match the ball's y-position
    vy = -P.control_k_vy*(robot(2)-point(2));

    % control angle to -pi/2
    theta_d = atan2(P.goal(2)-robot(2), P.goal(1)-robot(1));
    omega = -P.control_k_phi*(robot(3) - theta_d); 
    
    v = [vx; vy; omega];
end

%------------------------------------------
% utility - saturate_velocity
% 	saturate the commanded velocity 
%
function v = utility_saturate_velocity(v,P)
    if v(1) >  P.robot_max_vx,    v(1) =  P.robot_max_vx;    end
    if v(1) < -P.robot_max_vx,    v(1) = -P.robot_max_vx;    end
    if v(2) >  P.robot_max_vy,    v(2) =  P.robot_max_vy;    end
    if v(2) < -P.robot_max_vy,    v(2) = -P.robot_max_vy;    end
    if v(3) >  P.robot_max_omega, v(3) =  P.robot_max_omega; end
    if v(3) < -P.robot_max_omega, v(3) = -P.robot_max_omega; end
end


  