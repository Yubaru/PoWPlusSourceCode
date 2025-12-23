# RPG Battle System Documentation

## Table of Contents
1. [Overview](#overview)
2. [Character System](#character-system)
3. [Battle Mechanics](#battle-mechanics)
4. [Animation System](#animation-system)
5. [UI System](#ui-system)
6. [Skills and Items](#skills-and-items)
7. [Battle Flow](#battle-flow)
8. [Configuration](#configuration)
9. [Troubleshooting](#troubleshooting)

## Overview

The RPG battle system is a turn-based combat system integrated into the Doki Doki Literature Club mod. It features character battles with skills, items, animations, and strategic gameplay elements.

### Key Features
- Turn-based combat with initiative system
- Character skills and special abilities
- Item usage and inventory management
- Animated character sprites
- Status effects and buffs
- Blocking and defensive mechanics
- Boss patterns and special encounters

## Character System

### BattleCharacter Class

The core character class that handles all character-related functionality.

#### Properties
```python
class BattleCharacter:
    def __init__(self, name, hp, mp, skills, folder, sprite_pos=(0.5, 1.0), speed=5, anim_speed=0.3):
        self.name = name                    # Character name
        self.max_hp = hp                    # Maximum HP
        self.hp = hp                        # Current HP
        self.max_mp = mp                    # Maximum MP
        self.mp = mp                        # Current MP
        self.skills = {skill.name: skill for skill in skills}  # Available skills
        self.animations = {}                # Animation positions and settings
        self.status = {}                    # Active status effects
        self.blocking = False               # Blocking state
        self.sprite_pos = sprite_pos        # Screen position (x, y)
        self.folder = folder                # Animation folder name
        self.speed = speed                  # Turn order speed
        self.anim_speed = anim_speed        # Animation playback speed
        self.frame_counts = {}              # Animation frame counts
        self.attack_counter = 0             # Attack counter for boss patterns
        self.offense_buff = 0               # Offense buff duration
        self.defense_buff = 0               # Defense buff duration
        self.skill_cooldowns = {}           # Skill cooldown tracking
        self.consecutive_blocks = 0         # Consecutive block counter
        self.interrupted = False            # Interruption state
        self.status_resist = {}             # Status effect resistances
```

#### Core Methods

##### take_damage(damage)
Handles damage calculation and application with defensive modifiers.
```python
def take_damage(self, damage):
    multiplier = 1.0
    if self.blocking:
        multiplier *= 0.6  # Blocking reduces damage by 40%
        renpy.play(block_sound)
    else:
        renpy.play(damage_sound)
    
    if self.defense_buff > 0:
        multiplier *= 0.5  # Defense buff reduces damage by 50%
    
    if multiplier < 0.35:
        multiplier = 0.35  # Minimum damage multiplier
    
    damage = int(damage * multiplier)
    self.hp -= damage
    self.hp = max(0, self.hp)
    self.blocking = False
```

##### attack(target)
Performs a basic attack with critical hit mechanics.
```python
def attack(self, target):
    # Check if enemy is valid
    if enemy is None or not isinstance(enemy, BattleCharacter):
        return None
    
    # Critical hit: 12% base, guaranteed if enemy has 'exposed'
    if ("exposed" in enemy.status):
        crit = True
        try:
            del enemy.status["exposed"]
        except Exception:
            pass
    else:
        crit = (random.random() < 0.12)
    
    # Apply offense buff to damage
    damage_multiplier = 1.0
    if self.offense_buff > 0:
        damage_multiplier += 0.5
    
    base_damage = 12
    damage = int(base_damage * damage_multiplier * (2 if crit else 1))
    enemy.take_damage(damage)
    return "critical hit" if crit else None
```

##### perform_action(action, target)
Handles all character actions including attacks, skills, and items.
```python
def perform_action(self, action, target):
    if action == "attack":
        return self.attack(target)
    elif isinstance(action, Skill):
        # Handle skill execution
        if action.damage < 0 or action.effect in ["defense_up", "offense_up"]:
            # Healing or buff skills
            # ... implementation details
        else:
            # Damage skills
            # ... implementation details
    elif isinstance(action, Item):
        # Handle item usage
        # ... implementation details
    elif action == "block":
        self.blocking = True
        return "block"
```

##### apply_status()
Applies status effects and handles their duration.
```python
def apply_status(self):
    expired = []
    for effect in list(self.status):
        if effect == "poison":
            self.hp = max(0, self.hp - 5)
        elif effect == "burn":
            self.hp = max(0, self.hp - 3)
        elif effect == "freeze":
            # Freeze prevents the character from acting
            pass
        elif effect == "stun":
            # Stun prevents the character from acting
            pass
        elif effect == "offense_up":
            self.offense_buff = self.status[effect]
        elif effect == "defense_up":
            self.defense_buff = self.status[effect]
        
        self.status[effect] -= 1
        if self.status[effect] <= 0:
            expired.append(effect)
            # Reset buffs when expired
            if effect == "offense_up":
                self.offense_buff = 0
            elif effect == "defense_up":
                self.defense_buff = 0
    
    for e in expired:
        del self.status[e]
    
    # Passive MP regen
    self.mp = min(self.max_mp, self.mp + 2)
    
    # Decay resistances
    for k in list(self.status_resist.keys()):
        self.status_resist[k] = max(0.0, self.status_resist[k] - 0.10)
    
    # Clear interrupt
    self.interrupted = False
```

### Character Types

#### Player Characters
- **Jacko**: Main protagonist with balanced stats
- **Monika**: Support character with healing abilities

#### Enemy Characters
- **Yazzinator**: Boss character with special attack patterns
- Other enemies with varying abilities and stats

## Battle Mechanics

### Turn Order System

The battle uses a speed-based turn order system:
```python
# Turn order calculation
turn_order = sorted(all_characters, key=lambda c: c.speed, reverse=True)
```

### Battle States

#### Active States
- **Normal**: Character can perform any action
- **Blocking**: Character reduces incoming damage by 40%
- **Stunned**: Character cannot act for 1 turn
- **Frozen**: Character cannot act for 2 turns
- **Dead**: Character cannot act and has 0 HP

#### Status Effects
- **Poison**: Deals 5 damage per turn
- **Burn**: Deals 3 damage per turn
- **Stun**: Prevents action for 1 turn (50% chance to apply)
- **Freeze**: Prevents action for 2 turns (35% chance to apply)
- **Offense Up**: Increases damage by 50%
- **Defense Up**: Reduces incoming damage by 50%

### Damage Calculation

#### Base Damage Formula
```
Final Damage = Base Damage × Offense Multiplier × Critical Multiplier × Defense Multiplier
```

#### Multipliers
- **Offense Buff**: +50% damage
- **Critical Hit**: ×2 damage (12% chance, guaranteed if target is "exposed")
- **Blocking**: ×0.6 damage (40% reduction)
- **Defense Buff**: ×0.5 damage (50% reduction)
- **Minimum Damage**: 35% of original damage

### Boss Patterns

#### Yazzinator Special Mechanics
```python
# Obliteration charging
if (current_actor.attack_counter % RPG_RULES.get("boss_obliterate_interval", 4) == 0) and (not yazz_charge):
    yazz_charge = True
    battle_message = "[current_actor.name] is charging Obliteration! Disrupt or Block next turn!"

# Obliteration execution
elif yazz_charge:
    yazz_charge = False
    chosen_skill = current_actor.skills.get("Obliteration Technique", None)
    target = max(potential_targets, key=lambda c: c.hp)  # Target highest HP character
```

## Animation System

### Animation Registry

The system uses a centralized animation registry for all characters:

```python
RPG_ANIMATIONS = {
    "monika": {
        "idle":       {"frame_count": 3,  "framerate": 8.0,  "loop": True},
        "attack":     {"frame_count": 3,  "framerate": 12.0, "loop": True},
        "skill":      {"frame_count": 3,  "framerate": 12.0, "loop": False},
        "item":       {"frame_count": 3,  "framerate": 12.0, "loop": False},
        "block":      {"frame_count": 3,  "framerate": 12.0, "loop": True},
        "hurt":       {"frame_count": 3,  "framerate": 12.0, "loop": True},
        "victory":    {"frame_count": 3,  "framerate": 10.0, "loop": True},
        "dead":       {"frame_count": 3,  "framerate": 6.0,  "loop": True},
    },
    "yazzinator": {
        "idle":       {"frame_count": 14, "framerate": 14.0, "loop": True},
        "hurt":       {"frame_count": 7,  "framerate": 14.0, "loop": True},
        "cumbuster":  {"frame_count": 8,  "framerate": 10.0, "loop": True},
        "yazzpunch":  {"frame_count": 5,  "framerate": 16.0, "loop": True},
        "obliterate": {"frame_count": 4,  "framerate": 24.0, "loop": True, "loop_start": 1, "loop_end": 4},
    },
    "jacko": {
        "idle":    {"frame_count": 3, "framerate": 8.0,  "loop": True},
        "attack":  {"frame_count": 3, "framerate": 12.0, "loop": False},
        "block":   {"frame_count": 3, "framerate": 12.0, "loop": False},
        "hurt":    {"frame_count": 3, "framerate": 12.0, "loop": False},
        "item":    {"frame_count": 3, "framerate": 12.0, "loop": False},
        "skill":   {"frame_count": 3, "framerate": 12.0, "loop": False},
        "victory": {"frame_count": 3, "framerate": 10.0, "loop": True},
        "dead":    {"frame_count": 3, "framerate": 6.0,  "loop": False},
    },
}
```

### Animation Properties

Each animation can have the following properties:
- **frame_count**: Number of frames in the animation
- **framerate**: Playback speed in frames per second
- **loop**: Whether the animation loops
- **loop_start**: Starting frame for loop (optional)
- **loop_end**: Ending frame for loop (optional)

### Animation Function

```python
def play_character_anim(character, anim_name):
    if character.name.lower() == "jacko":
        return  # Jacko animations are disabled
    
    global _current_anim_by_char
    last_anim = _current_anim_by_char.get(character.name)
    if last_anim == anim_name:
        return  # Avoid redundant animation calls
    
    renpy.hide_screen("character_anim_" + character.name.lower())
    renpy.show_screen("character_anim_" + character.name.lower(), char=character, anim=anim_name)
    _current_anim_by_char[character.name] = anim_name
```

### Animation Screen

```python
screen _rpg_anim_base(char, anim):
    zorder 90
    modal False
    
    $ folder = char.folder
    $ cfg_anim = get_rpg_anim_config(folder, anim)
    $ cfg_idle = get_rpg_anim_config(folder, "idle")
    $ base_path = "mod_assets/images/games/rpg/{}/".format(folder)
    
    # Choose requested or fallback to idle if missing
    $ _anim_to_use = anim if cfg_anim else "idle"
    $ _cfg_to_use = cfg_anim if cfg_anim else cfg_idle
    $ _frame_count = (_cfg_to_use["frame_count"] if _cfg_to_use else 1)
    
    # Use persistent sequencer for all animations
    use png_sequence_anim(
        name="{}_{}".format(folder, _anim_to_use),
        frame_count=_frame_count,
        base_path=base_path,
        base_name=_anim_to_use,
        framerate=framerate,
        zero_pad=1,
        extension=".png",
        loop=loop,
        loop_start=loop_start,
        loop_end=loop_end,
        x=pos[0],
        y=pos[1],
        separator="",
        is_modal=False,
        z=90,
        anchor_x=0.5,
        anchor_y=1.0,
    )
```

## UI System

### Battle UI Structure

The battle UI consists of several screens:

#### Main Battle UI (`battle_ui`)
- Character action menus (Attack, Skill, Item, Block)
- Dynamic menu states based on active character
- Modal screen detection and button disabling

#### Battle HUD (`battle_hud`)
- Turn order display
- Battle message display
- Character status information

#### Character Stats (`battle_stats`)
- HP and MP bars for all characters
- Status effect indicators
- Active character highlighting

### Modal Screen System

The UI includes a modal screen detection system to prevent unwanted interactions:

```python
# Check if any modal screen is active
$ modal_screen_active = False
python:
    try:
        modal_screen_active = any([
            renpy.get_screen("skill_select"),
            renpy.get_screen("item_select"),
            renpy.get_screen("target_select"),
            renpy.get_screen("skill_target_select"),
            renpy.get_screen("enemy_target_select")
        ])
    except:
        modal_screen_active = False
```

### Button Sensitivity

All buttons in the battle UI respect modal screen states:

```python
textbutton "Attack" action (Return("attack") if jacko_active else NullAction()) 
    style "battle_button" text_style "battle_button_text" 
    xsize 150 ysize 50 
    sensitive (jacko_active and not modal_screen_active)
```

### Selection Screens

#### Skill Selection (`skill_select`)
```python
screen skill_select(skills, actor=None):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 20
        background "#2C3E5090"
        
        has vbox spacing 10
        text "Choose a Skill" size 28 color "#F1C40F" xalign 0.5

        for skill in skills.values():
            hbox:
                spacing 10
                textbutton "[skill.name]" action Return(skill.name) 
                    style "battle_button" text_style "battle_button_text" 
                    xsize 200 
                    sensitive (actor is None or actor.mp >= skill.cost)
                text "MP: [skill.cost]" size 18 color "#3498DB" yalign 0.5
                if skill.effect:
                    text "Effect: [skill.effect]" size 18 color "#9B59B6" yalign 0.5

        textbutton "Back" action Return(None) 
            style "battle_button" text_style "battle_button_text" 
            xsize 150 ysize 40
```

#### Enemy Target Selection (`enemy_target_select`)
```python
screen enemy_target_select(enemies):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 20
        background "#2C3E5090"
        has vbox spacing 10
        text "Choose Enemy Target" size 28 color "#F1C40F" xalign 0.5
        for e in enemies:
            textbutton "[e.name] ([e.hp]/[e.max_hp] HP)" action Return(e) 
                style "battle_button" text_style "battle_button_text"
        textbutton "Back" action Return(None) 
            style "battle_button" text_style "battle_button_text" 
            xsize 150 ysize 40
```

## Skills and Items

### Skill Class

```python
class Skill:
    def __init__(self, name, cost, damage, effect=None, duration=3, cooldown=0):
        self.name = name        # Skill name
        self.cost = cost        # MP cost
        self.damage = damage    # Damage amount (negative for healing)
        self.effect = effect    # Status effect applied
        self.duration = duration # Effect duration
        self.cooldown = cooldown # Cooldown turns
```

### Item Class

```python
class Item:
    def __init__(self, name, heal_amount=0, revive=False, mp_restore=0):
        self.name = name        # Item name
        self.heal_amount = heal_amount  # HP restoration amount
        self.revive = revive    # Whether item can revive
        self.mp_restore = mp_restore    # MP restoration amount
```

### Inventory System

```python
class Inventory:
    def __init__(self):
        self.items = {}  # Dictionary of items and counts

    def add_item(self, item, amount=1):
        if item.name in self.items:
            self.items[item.name]["count"] += amount
        else:
            self.items[item.name] = {"item": item, "count": amount}

    def use_item(self, item_name):
        if item_name in self.items and self.items[item_name]["count"] > 0:
            self.items[item_name]["count"] -= 1
            if self.items[item_name]["count"] == 0:
                del self.items[item_name]
            return True
        return False

    def get_items(self):
        return [(entry["item"], entry["count"]) for entry in self.items.values()]
```

## Battle Flow

### Main Battle Loop

The battle system follows this flow:

1. **Battle Initialization**
   ```python
   label battle_start:
       # Initialize battle variables
       $ turn_order = sorted(all_characters, key=lambda c: c.speed, reverse=True)
       $ current_turn_index = 0
       $ turn_index = 0
   ```

2. **Turn Processing**
   ```python
   while turn_index < len(turn_order):
       $ current_turn_name = turn_order[turn_index]
       $ current_turn_index = turn_index
       
       # Resolve current actor
       python:
           name_to_char = {c.name.lower(): c for c in all_characters}
           current_actor = name_to_char.get(current_turn_name)
   ```

3. **Action Selection**
   - Player characters: Call `choose_action` label
   - Enemy characters: AI-driven action selection

4. **Action Execution**
   - Attack actions
   - Skill actions
   - Item actions
   - Block actions

5. **Turn Completion**
   ```python
   $ turn_index += 1
   ```

### Action Selection Flow

```python
label choose_action:
    $ result = renpy.call_screen("battle_ui")

    # Handle inline skill selection by name
    if isinstance(result, str) and result in current_actor.skills:
        $ chosen_skill = current_actor.skills[result]
        if current_actor.mp < chosen_skill.cost:
            $ battle_message = "[current_actor.name] doesn't have enough MP!"
            jump choose_action
        
        if chosen_skill.damage < 0 or chosen_skill.effect in ["defense_up", "offense_up"]:
            $ target_choice = renpy.call_screen("skill_target_select", allies=[p for p in party_list], skill_name=result)
            if target_choice is None:
                jump choose_action
            if isinstance(target_choice, BattleCharacter):
                $ planned_action = chosen_skill
                $ planned_target = target_choice
                return
        else:
            $ planned_action = chosen_skill
            $ planned_target = None  # will pick an enemy via enemy_target_select
            return

    # Handle other action types...
```

### Error Handling

The system includes comprehensive error handling for:
- Invalid targets
- Insufficient MP
- Missing items
- Cancelled actions
- Invalid character states

## Configuration

### RPG Rules Configuration

```python
RPG_RULES = {
    "boss_obliterate_interval": 4,  # Turns between Obliteration charges
    "min_damage_multiplier": 0.35,  # Minimum damage multiplier
    "block_damage_reduction": 0.6,  # Block damage reduction
    "defense_buff_reduction": 0.5,  # Defense buff damage reduction
    "offense_buff_multiplier": 1.5, # Offense buff damage multiplier
    "critical_hit_chance": 0.12,    # Base critical hit chance
    "critical_hit_multiplier": 2.0, # Critical hit damage multiplier
    "mp_regen_per_turn": 2,         # MP regeneration per turn
    "status_resist_decay": 0.10,    # Status resistance decay per turn
}
```

### Animation Configuration

Animation settings are defined in the `RPG_ANIMATIONS` registry with frame counts, framerates, and loop settings for each character and animation type.

### Character Configuration

Character stats and abilities are configured when creating `BattleCharacter` instances:

```python
# Example character creation
jacko = BattleCharacter(
    name="Jacko",
    hp=100,
    mp=50,
    skills=[skill1, skill2, skill3],
    folder="jacko",
    sprite_pos=(0.3, 1.0),
    speed=8,
    anim_speed=0.3
)
```

## Troubleshooting

### Common Issues

#### 1. Animation Not Playing
- Check if animation files exist in the correct folder
- Verify animation registry configuration
- Ensure character folder name matches registry key
- Check if animation is disabled for specific characters (e.g., Jacko)

#### 2. Battle UI Not Responding
- Check if modal screens are properly configured
- Verify button sensitivity conditions
- Ensure proper screen hierarchy and z-order

#### 3. Skills Not Working
- Verify skill configuration (cost, damage, effects)
- Check MP requirements
- Ensure target selection is working correctly
- Verify skill execution in `perform_action` method

#### 4. Turn Order Issues
- Check character speed values
- Verify turn order calculation
- Ensure all characters are properly initialized

#### 5. Damage Calculation Problems
- Check damage multipliers and buffs
- Verify defensive mechanics (blocking, defense buffs)
- Ensure proper damage application in `take_damage` method

### Debug Tools

#### Animation Debug
```python
# Debug animation calls
if character.name.lower() == "yazzinator" and anim_name == "hurt":
    print("DEBUG: Playing Yazzinator hurt animation")
```

#### Battle State Debug
```python
# Print current battle state
print(f"Current actor: {current_actor.name}")
print(f"Turn order: {[c.name for c in turn_order]}")
print(f"Battle message: {battle_message}")
```

### Performance Considerations

1. **Animation Optimization**
   - Use appropriate frame counts and framerates
   - Implement animation caching for frequently used animations
   - Avoid redundant animation calls

2. **UI Responsiveness**
   - Use modal screens appropriately
   - Implement proper button sensitivity
   - Avoid blocking operations in UI updates

3. **Memory Management**
   - Clean up animation resources when not needed
   - Properly dispose of screen elements
   - Monitor memory usage during long battles

### Best Practices

1. **Character Design**
   - Balance HP, MP, and speed stats
   - Design skills with appropriate costs and effects
   - Consider character roles and synergies

2. **Battle Design**
   - Create engaging boss patterns
   - Balance difficulty progression
   - Implement meaningful choices and strategies

3. **UI/UX Design**
   - Provide clear feedback for all actions
   - Implement intuitive controls
   - Ensure accessibility and usability

4. **Code Organization**
   - Separate concerns (battle logic, UI, animations)
   - Use consistent naming conventions
   - Implement proper error handling
   - Document complex systems and interactions

---

This documentation covers the complete RPG battle system implementation. For specific implementation details, refer to the source code files in the `game/custom_scripts/` directory.
